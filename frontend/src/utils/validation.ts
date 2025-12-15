interface ValidationErrors {
  [key: string]: string;
}

const validateEmail = (email: string): boolean => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

const validatePassword = (password: string): string | null => {
  if (password.length < 8) {
    return 'Password must be at least 8 characters long';
  }
  if (!/[A-Z]/.test(password)) {
    return 'Password must contain at least one uppercase letter';
  }
  if (!/[a-z]/.test(password)) {
    return 'Password must contain at least one lowercase letter';
  }
  if (!/\d/.test(password)) {
    return 'Password must contain at least one number';
  }
  return null;
};

const validateForm = (formData: any, rules: { [key: string]: (value: any) => string | null }): ValidationErrors | null => {
  const errors: ValidationErrors = {};

  Object.keys(rules).forEach(field => {
    const error = rules[field](formData[field]);
    if (error) {
      errors[field] = error;
    }
  });

  return Object.keys(errors).length > 0 ? errors : null;
};

export { validateEmail, validatePassword, validateForm };