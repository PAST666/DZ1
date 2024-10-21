from django.utils import timezone
from datetime import timedelta
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
        
        # Увеличиваем счетчик только если прошло более 30 минут с последнего визита
        if created or (timezone.now() - visitor.last_visited_at) > timedelta(minutes=30):
            visitor.views += 1
        
        visitor.last_visited_at = timezone.now()
        visitor.save()
        
        response = self.get_response(request)
        return response