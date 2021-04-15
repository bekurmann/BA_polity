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
        exclude = ["created_at", "updated_at", "additional_information", "content_all", "content_motivation",
                    "content_inquiries", "joint_signatories_count", "anon_yes", "anon_no", "anon_abstinence", 
                    "recommendation", "transformation_recommendation", "content_response", "discussion_desired",
                    "transformation_postulat", "commission", "joint_signatories", "personalised_yes", 
                    "personalised_no", "personalised_abstinence",]

class AffairDetailSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (detail)
    """

    affair_type = serializers.CharField(source='get_affair_type_display')

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
    affair = AffairListSerializer(read_only=True)

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