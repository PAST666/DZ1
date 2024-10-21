from .models import SiteVisitor

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_id = request.session.session_key
        if not session_id:
            request.session.save()
            session_id = request.session.session_key

        visitor, created = SiteVisitor.objects.get_or_create(session_id=session_id)
        visitor.views += 1
        visitor.save()
        
        response = self.get_response(request)
        return response