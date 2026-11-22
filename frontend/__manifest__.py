{
    "name": "Task Management Home",
    "version": "18.0.1.0.0",
    "category": "Hidden",
    "summary": "Simple home page with three navigation buttons",
    "depends": ["web"],
    "data": [
        "views/menu_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "frontend/static/src/home_page/home_page.js",
            "frontend/static/src/home_page/home_page.xml",
            "frontend/static/src/home_page/home_page.scss",
        ],
    },
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
