from flask_restx import Namespace, Resource, fields

from conduit.models.project import Project


ns = Namespace("projects")
project_model = ns.model("Project", {
    'code': fields.String,
    'provider': fields.String,
    'name': fields.String
})


@ns.route("/<string:code>")
class ProjectByCode(Resource):
    @ns.marshal_with(project_model)
    def get(self, code):
        project = Project.query.filter_by(code=code).first_or_404()
        return project