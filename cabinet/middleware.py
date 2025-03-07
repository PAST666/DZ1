from django.utils import timezone
from cabinet.models import SiteVisitor

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not any(request.path.startswith(prefix) for prefix in ["/static/", "/media/", "/admin/"]):
            session_id = request.session.session_key
            if not session_id:
                request.session.save()
                session_id = request.session.session_key

            visitor, created = SiteVisitor.objects.get_or_create(session_id=session_id)
        
            if created:
                visitor.first_visited_at = timezone.now()
                visitor.last_visited_at = timezone.now()
                visitor.views = 1
                visitor.save()
            else:
                visitor.update_visit()
        
        
        response = self.get_response(request)
        return response