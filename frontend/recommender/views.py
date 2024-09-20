from django.shortcuts import render
from .forms import SymptomForm
from .models import Symptom, Disease, SymptomDiseaseRelation
from django.db.models import Sum

def health_recommender(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms'].lower().split(',')
            symptoms = [s.strip() for s in symptoms]

            # Get matching symptoms from the database
            matching_symptoms = Symptom.objects.filter(name__in=symptoms)

            # Get diseases related to these symptoms
            disease_weights = SymptomDiseaseRelation.objects.filter(symptom__in=matching_symptoms)\
                .values('disease')\
                .annotate(total_weight=Sum('weight'))\
                .order_by('-total_weight')

            if disease_weights:
                top_disease = Disease.objects.get(id=disease_weights[0]['disease'])
                context = {
                    'form': form,
                    'disease': top_disease,
                }
                return render(request, 'recommender/results.html', context)
    else:
        form = SymptomForm()
    
    return render(request, 'recommender/index.html', {'form': form})