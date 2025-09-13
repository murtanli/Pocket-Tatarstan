from django.db import models


class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.login


class Level(models.Model):
    """Уровень с фоном"""
    name = models.CharField(max_length=100)
    level_image = models.ImageField(upload_to="levels/", blank=True, null=True)
    star_pr = models.IntegerField(default=0)  # количество звезд

    def __str__(self):
        return self.name


class Object(models.Model):
    """Черный объект на уровне (например, здание)"""
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="level_objects")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (Level {self.level_id})"


class ObjectPart(models.Model):
    """Часть объекта (кусочек для вставки)"""
    parent = models.ForeignKey(Object, on_delete=models.CASCADE, related_name="parts")
    image = models.ImageField(upload_to="parts/")  # картинка куска
    center_x = models.FloatField()  # координаты центра
    center_y = models.FloatField()

    def __str__(self):
        return f"Part {self.id} of {self.parent.name}"


class Profile(models.Model):
    """Проифль пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    email = models.EmailField(max_length=100)
    rating = models.FloatField(default=0)
    last_level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    stars = models.IntegerField(default=0)

    def __str__(self):
        return f"Profile of {self.user.login}"


class Progress(models.Model):
    """Прогресс игрока"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="progress")
    collected_parts = models.JSONField(default=list)  # [part_id1, part_id2, ...]
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.login} - {self.level.name}"

class History_images(models.Model):
    """Хранение озображений исторической справки"""
    name = models.CharField(max_length=20)
    history_image = models.ImageField(upload_to="history_image/", blank=True, null=True)

class HistoryLevel(models.Model):
    """Историческая справка об объекте"""
    level = models.OneToOneField(Level, on_delete=models.CASCADE, related_name="history")
    text = models.TextField()
    image = models.ManyToManyField(History_images, blank=True)

    def __str__(self):
        return f"History of {self.object.name}"

