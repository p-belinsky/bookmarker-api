template = {
  "swagger": "2.0",
  "info": {
    "title": "Bookmarks API",
    "description": "API for my bookmarks",
    "contact": {
      "responsibleOrganization": "",
      "responsibleDeveloper": "Phil Belinsky",
      "email": "philbeinsky@yahoo.com",
      "url": "",
    },
    "termsOfService": "",
    "version": "1.0"
  },
  "basePath": "/",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],


}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}