from django.contrib import admin

from posts import tasks
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'title', 'created')
    search_fields = ('title', 'user__username', 'user__email')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            tasks.reboot_cache_main()
