"""RightsGuide – GTK4/Adwaita-app för guide till LSS, assistans och vårdstöd."""

import json
import os
import sys

import gi
from rightsguide.i18n import _

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, Gtk, Pango  # noqa: E402

from rightsguide.data import CATEGORIES  # noqa: E402

HISTORY_PATH = os.path.join(
    os.environ.get("XDG_DATA_HOME", os.path.expanduser("~/.local/share")),
    "rightsguide",
    "history.json",
)


def load_history():
    """Ladda läshistorik från JSON."""
    try:
        with open(HISTORY_PATH) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"read": []}


def save_history(history):
    """Spara läshistorik till JSON."""
    os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)
    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


class RightsGuideApp(Adw.Application):
    """Huvudapplikation."""

    def __init__(self):
        super().__init__(
            application_id="se.rightsguide.app",
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
        )
        self.history = load_history()

    def do_activate(self):
        win = RightsGuideWindow(application=self)
        win.present()


class RightsGuideWindow(Adw.ApplicationWindow):
    """Huvudfönster med navigering mellan kategorier och frågor."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title("RightsGuide")
        self.set_default_size(480, 720)

        self.history = self.get_application().history

        # Huvudlayout
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(self.main_box)

        # Header bar
        header = Adw.HeaderBar()
        self.back_btn = Gtk.Button(icon_name="go-previous-symbolic")
        self.back_btn.connect("clicked", self._on_back)
        self.back_btn.set_visible(False)
        header.pack_start(self.back_btn)

        self.title_widget = Adw.WindowTitle(
            title=_("RightsGuide",
            subtitle=_("Guide to your rights",
        )
        header.set_title_widget(self.title_widget)
        self.main_box.append(header)

        # Navigation stack
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(200)
        self.main_box.append(self.stack)

        # Bygg vyer
        self._build_home()
        for cat in CATEGORIES:
            self._build_category_page(cat)
            for i, qa in enumerate(cat["qa"]):
                self._build_answer_page(cat, i, qa)

        self.stack.set_visible_child_name("home")

    # ── Hemskärm ──────────────────────────────────────────────

    def _build_home(self):
        scroll = Gtk.ScrolledWindow(vexpand=True)
        clamp = Adw.Clamp(maximum_size=600)
        scroll.set_child(clamp)

        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=16,
            margin_top=24,
            margin_bottom=24,
            margin_start=16,
            margin_end=16,
        )
        clamp.set_child(box)

        # Välkomsttext
        welcome = Gtk.Label(
            label=_("Welcome!",
            css_classes=["title-1"],
        )
        box.append(welcome)

        intro = Gtk.Label(
            label=(
                "Här hittar du enkel information om dina rättigheter "
                "till stöd och hjälp i Sverige."
            ),
            wrap=True,
            justify=Gtk.Justification.CENTER,
            css_classes=["body"],
            margin_bottom=8,
        )
        box.append(intro)

        # Kategoriknappar
        for cat in CATEGORIES:
            btn = self._make_category_button(cat)
            box.append(btn)

        self.stack.add_named(scroll, "home")

    def _make_category_button(self, cat):
        """Skapa en stor, lättläst kategoriknapp."""
        box = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=16,
            margin_top=4,
            margin_bottom=4,
        )

        icon = Gtk.Label(
            label=cat["icon"],
            css_classes=["title-1"],
        )
        box.append(icon)

        text_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        title = Gtk.Label(
            label=cat["title"],
            css_classes=["title-3"],
            xalign=0,
            ellipsize=Pango.EllipsizeMode.END,
        )
        text_box.append(title)

        desc = Gtk.Label(
            label=cat["description"],
            css_classes=["body"],
            xalign=0,
            ellipsize=Pango.EllipsizeMode.END,
        )
        desc.add_css_class("dim-label")
        text_box.append(desc)

        box.append(text_box)

        btn = Gtk.Button(css_classes=["card"], child=box)
        btn.set_hexpand(True)
        btn.connect("clicked", lambda _b, c=cat: self._navigate_to(c["id"]))
        return btn

    # ── Kategorisida ──────────────────────────────────────────

    def _build_category_page(self, cat):
        scroll = Gtk.ScrolledWindow(vexpand=True)
        clamp = Adw.Clamp(maximum_size=600)
        scroll.set_child(clamp)

        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=12,
            margin_top=24,
            margin_bottom=24,
            margin_start=16,
            margin_end=16,
        )
        clamp.set_child(box)

        header_label = Gtk.Label(
            label=f"{cat['icon']}  {cat['title']}",
            css_classes=["title-2"],
            wrap=True,
        )
        box.append(header_label)

        desc = Gtk.Label(
            label=cat["description"],
            css_classes=["body"],
            wrap=True,
            margin_bottom=8,
        )
        desc.add_css_class("dim-label")
        box.append(desc)

        # Frågeknappar
        for i, qa in enumerate(cat["qa"]):
            qa_key = f"{cat['id']}_{i}"
            is_read = qa_key in self.history.get("read", [])

            btn_box = Gtk.Box(
                orientation=Gtk.Orientation.HORIZONTAL, spacing=12
            )
            q_icon = Gtk.Label(label=_("✅" if is_read else "❓")
            btn_box.append(q_icon)
            q_label = Gtk.Label(label=qa["q"], xalign=0, wrap=True)
            q_label.set_hexpand(True)
            btn_box.append(q_label)

            arrow = Gtk.Image(icon_name="go-next-symbolic")
            btn_box.append(arrow)

            btn = Gtk.Button(css_classes=["card"], child=btn_box)
            btn.set_hexpand(True)
            btn.connect(
                "clicked",
                lambda _b, cid=cat["id"], idx=i: self._navigate_to(
                    f"{cid}_q{idx}"
                ),
            )
            box.append(btn)

        self.stack.add_named(scroll, cat["id"])

    # ── Svarsida ──────────────────────────────────────────────

    def _build_answer_page(self, cat, idx, qa):
        scroll = Gtk.ScrolledWindow(vexpand=True)
        clamp = Adw.Clamp(maximum_size=600)
        scroll.set_child(clamp)

        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=16,
            margin_top=24,
            margin_bottom=24,
            margin_start=16,
            margin_end=16,
        )
        clamp.set_child(box)

        q_label = Gtk.Label(
            label=qa["q"],
            css_classes=["title-2"],
            wrap=True,
            xalign=0,
        )
        box.append(q_label)

        sep = Gtk.Separator()
        box.append(sep)

        a_label = Gtk.Label(
            label=qa["a"],
            css_classes=["body"],
            wrap=True,
            xalign=0,
            use_markup=False,
            selectable=True,
        )
        box.append(a_label)

        page_name = f"{cat['id']}_q{idx}"
        self.stack.add_named(scroll, page_name)

    # ── Navigering ────────────────────────────────────────────

    def _navigate_to(self, page_name):
        self.stack.set_visible_child_name(page_name)
        self.back_btn.set_visible(True)

        # Uppdatera titel
        if "_q" in page_name:
            cat_id, q_part = page_name.split("_q")
            idx = int(q_part)
            cat = next(c for c in CATEGORIES if c["id"] == cat_id)
            self.title_widget.set_title(cat["title"])
            self.title_widget.set_subtitle(cat["qa"][idx]["q"])
            # Spara läshistorik
            key = f"{cat_id}_{idx}"
            if key not in self.history.get("read", []):
                self.history.setdefault("read", []).append(key)
                save_history(self.history)
        else:
            cat = next(c for c in CATEGORIES if c["id"] == page_name)
            self.title_widget.set_title(cat["title"])
            self.title_widget.set_subtitle(cat["description"])

        self._nav_stack.append(page_name)

    @property
    def _nav_stack(self):
        if not hasattr(self, "_nav_history"):
            self._nav_history = ["home"]
        return self._nav_history

    def _on_back(self, _btn):
        if len(self._nav_stack) > 1:
            self._nav_stack.pop()
            prev = self._nav_stack[-1]
            self.stack.set_visible_child_name(prev)

            if prev == "home":
                self.back_btn.set_visible(False)
                self.title_widget.set_title("RightsGuide")
                self.title_widget.set_subtitle(_("Guide to your rights"))
            elif "_q" not in prev:
                cat = next(c for c in CATEGORIES if c["id"] == prev)
                self.title_widget.set_title(cat["title"])
                self.title_widget.set_subtitle(cat["description"])


def main():
    """Starta applikationen."""
    app = RightsGuideApp()
    return app.run(sys.argv)


if __name__ == "__main__":
    raise SystemExit(main())
