import graphene
from graphene_django import DjangoObjectType
from hrd_kantor.models import Profile, Perusahaan

class PerusahaanCategory(DjangoObjectType):
    class Meta:
        model = Perusahaan
        fields = ('id','npp','nama')

class ProfileCategory(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ('id','user','nama','nik','tgl_lahir','tempat_lahir',
            'propic','npp','is_hrd')

class Query(graphene.ObjectType):
    all_companies = graphene.List(PerusahaanCategory)
    all_profiles = graphene.List(ProfileCategory)

    def resolve_all_companies(root, info, **kwargs):
        
        return Perusahaan.objects.all()
    
    def resolve_all_profiles(root, info, **kwargs):
        return Profile.objects.all()

schema = graphene.Schema(query=Query)