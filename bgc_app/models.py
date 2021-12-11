from django.db import models


class BoardGame(models.Model):
    """Something specific learned about a topic."""
    #owner = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
