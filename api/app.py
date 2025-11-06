from flask import Flask, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)

# Osnovna Swagger meta
app.config["SWAGGER"] = {
    "title": "RPO Portfolio API",
    "uiversion": 3
}
swagger = Swagger(app)


@app.get("/api/portfolio")
@swag_from({
    "tags": ["Portfolio"],
    "summary": "Osnovne informacije o portfelju",
    "responses": {
        200: {
            "description": "Podatki o avtorju portfelja",
            "content": {
                "application/json": {
                    "example": {
                        "author": "Anastasija Temova",
                        "email": "temanastasa@gmail.com",
                        "github": "https://github.com/ATemova"
                    }
                }
            }
        }
    }
})
def get_portfolio():
    return jsonify({
        "author": "Anastasija Temova",
        "email": "temanastasa@gmail.com",
        "github": "https://github.com/ATemova"
    })


@app.get("/api/projects")
@swag_from({
    "tags": ["Projects"],
    "summary": "Seznam projektov",
    "responses": {
        200: {
            "description": "Kratek seznam projektov",
            "content": {
                "application/json": {
                    "example": [
                        {"title": "Animal Faces Recognition", "tech": ["Python", "ML"]},
                        {"title": "BookFlow", "tech": ["Java"]},
                        {"title": "Heat Simulator", "tech": ["Java"]}
                    ]
                }
            }
        }
    }
})
def get_projects():
    return jsonify([
        {"title": "Animal Faces Recognition", "tech": ["Python", "ML"]},
        {"title": "BookFlow", "tech": ["Java"]},
        {"title": "Heat Simulator", "tech": ["Java"]}
    ])


if __name__ == "__main__":
    # Lokalni zagon
    app.run(debug=True)