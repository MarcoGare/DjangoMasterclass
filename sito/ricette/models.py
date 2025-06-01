from django.db import models
from django.contrib.auth.models import User

class Concorrente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100, default="Sconosciuto", blank=True)
    professione = models.CharField(max_length=100, default="Non specificata", blank=True)
    eta = models.PositiveIntegerField(default=0)  
    foto = models.ImageField(upload_to='immagini/foto_concorrenti/', default='immagini/default_concorrente.jpg')

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.professione})"

class Chef(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100, default="Sconosciuto", blank=True)
    stelle_michelin = models.PositiveIntegerField(default=0)
    foto = models.ImageField(upload_to='immagini/foto_chef/', default='immagini/default_chef.jpg')

    def __str__(self):
        return f"{self.nome} {self.cognome} ⭐️ {self.stelle_michelin}"

class Ricetta(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.TextField()
    immagine = models.ImageField(upload_to='immagini/')
    concorrente = models.ForeignKey(Concorrente, on_delete=models.CASCADE, null=True, blank=True)
    giudici = models.ManyToManyField(Chef, related_name='ricette_giudicate')

    def __str__(self):
        return self.titolo

class Preferito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ricetta = models.ForeignKey(Ricetta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.ricetta.titolo}"
