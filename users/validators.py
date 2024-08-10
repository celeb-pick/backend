from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError


class CustomMinimumLengthValidator(MinimumLengthValidator):
    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                f"비밀번호는 {self.min_length}자 이상이어야 합니다.",
                code="password_too_short",
                params={"min_length": self.min_length},
            )
