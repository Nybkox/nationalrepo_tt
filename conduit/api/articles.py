from flask_restx import Namespace, Resource, fields

from conduit.models.article import Article
from conduit.models.author import Author
from conduit.api.projects import project_model


ns = Namespace('articles')
article_model = ns.model("Article", {
    'title': fields.String,
    'authors': fields.List(fields.String),
    'funding': fields.Nested(project_model, as_list=True)
})


@ns.route('/<int:organization_code>')
class ArticleByOrganization(Resource):
    @ns.marshal_list_with(article_model)
    def get(self, organization_code):
        articles = Article.query.filter(Article.organization.has(code=organization_code)).all()
        return articles


@ns.route('/<int:organization_code>/<string:author_name>')
class ArticleByOrganizationAndAuthor(Resource):
    @ns.marshal_list_with(article_model)
    def get(self, organization_code, author_name):
        q = Article.query.filter(Article.organization.has(code=organization_code))
        articles = q.filter(Article.authors.any(Author.name.like(f'{author_name}%'))).all()
        return articles
