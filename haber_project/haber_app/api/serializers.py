from rest_framework import serializers
from haber_app.models import Makale


class MakaleSerilazer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    yazar=serializers.CharField()
    baslik=serializers.CharField()
    aciklama=serializers.CharField()
    metin=serializers.CharField() 
    sehir=serializers.CharField()
    yayınlanma_tarihi=serializers.DateField()
    aktif=serializers.BooleanField()
    yaratılnma_tarihi=serializers.DateTimeField(read_only=True)
    güncellenme_tarihi=serializers.DateTimeField(read_only=True)

    def create(self,validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.yazar=validated_data.get('yazar',instance.yazar)
        instance.baslik=validated_data.get('baslik',instance.baslik)
        instance.aciklama=validated_data.get('aciklama',instance.aciklama)
        instance.metin=validated_data.get('metin',instance.metin)
        instance.sehir=validated_data.get('sehir',instance.sehir)
        instance.yayınlanma_tarihi=validated_data.get('yayınlanma_tarihi',instance.yayınlanma_tarihi)
        instance.aktif=validated_data.get('aktif',instance.aktif)
        instance.save()
        return instance
    
    def validate(self,data):
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError(' Başlık ve açıklama alanları aynı olamaz')
        
        elif data['metin'] == data['aciklama']:
            raise serializers.ValidationError('metin ve açıklama alanları aynı olamaz')
        return data 
    
    def validate_baslik(self,value): 
        if len(value)<20:
            raise serializers.ValidationError(f'başlık alanı min 20 olamlı siz {len(value)} karakter kullandınız')
        return value
    



