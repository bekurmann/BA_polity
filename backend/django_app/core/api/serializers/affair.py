from rest_framework import serializers

# import models
from core.models import Affair, AffairDebate, AffairFile

# ************************************************************
# Affair
# ************************************************************

class AffairListSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (list)
    """

    class Meta:
        model = Affair
        exclude = ["created_at", "updated_at",]

class AffairDetailSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (detail)
    """

    class Meta:
        model = Affair
        exclude = ["created_at", "updated_at",]

# ************************************************************
# AffairDebate
# ************************************************************
class AffairDebateListSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (list)
    """

    class Meta:
        model = AffairDebate
        exclude = ["created_at", "updated_at",]

class AffairDebateDetailSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (detail)
    """

    class Meta:
        model = AffairDebate
        exclude = ["created_at", "updated_at",]
# ************************************************************
# AffairFile
# ************************************************************
class AffairFileListSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (list)
    """

    class Meta:
        model = AffairFile
        exclude = ["created_at", "updated_at",]

class AffairFileDetailSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (list)
    """

    class Meta:
        model = AffairFile
        exclude = ["created_at", "updated_at",]