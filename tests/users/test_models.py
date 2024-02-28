import pytest

def test_user_str(base_user):
    """"Test the custom user mode string representation"""
    assert base_user.__str__() == f"{base_user.username}"

def test_user_short_name(base_user):
    """Test that the user models get_short_name method works"""
    short_name = f"{base_user.username}"
    assert base_user.get_short_name == short_name

def test_user_full_name(base_user):
    """Test that the user models get_full_name method works"""
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == full_name

def test_base_user_email_is_normalized(base_user):
    """Test that the new user's email is normalized"""
    email = f"admin@GMAIL.COM"
    assert base_user.email == email.lower()

def test_super_user_email_is_normalized(super_user):
    """Test that the admin user email is normalized"""
    email = f"admin@GMAIL.COM"
    assert super_user.email == email.lower()

def test_super_user_is_not_staff(user_factory):
    """Test that an error is raised when a admin user has is_staff set to false"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True,is_staff=False)
    assert str(err.value) == "is staff must be true for admin user"

def test_super_user_is_not_superuser(user_factory):
    """Test error is raised when admin user has is_superuser set to False"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False,is_staff=True)
    assert str(err.value) == "is superuser must be true for admin user"

def test_create_user_with_no_email(user_factory):
    """Test that creating a new user with no email address raises a error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: An email address is required"

def test_create_user_with_no_username(user_factory):
    """Test that creating a new user with no username raises a error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "Users must submit a username"

def test_create_user_with_no_first_name(user_factory):
    """"Test creating a new user without a firstname raises a error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "Users must submit a first_name"

def test_create_user_with_no_last_name(user_factory):
    """"Test creating a new user without a lastname raises a error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "Users must submit a last_name"

def test_create_superuser_with_no_email(user_factory):
    """Test creating a superuser with no email address raises a error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None,is_superuser=True,is_staff=True)
    assert str(err.value) == "Admin Account: An email address is required"

def test_create_superuser_with_no_password(user_factory):
    """Test creating a superuser with no password raises a error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None,is_superuser=True,is_staff=True)
    assert str(err.value) == "Superuser must have a password"

def test_user_email_incorrect(user_factory):
    """Test a error is raised if a not valid email is provided"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email="realest.com")
    assert str(err.value) == "You must provide a valid email address"

