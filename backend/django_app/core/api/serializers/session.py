class SessionSerializer(serializers.ModelSerializer):
    """
    model serializer for session
    """
    class Meta:
        model = Session
        exclude = ['created_at', 'updated_at', ]