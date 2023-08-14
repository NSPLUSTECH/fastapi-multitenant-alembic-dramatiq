from fastapi.testclient import TestClient
from app.main import app
from app.models.auth_models import LoginRequest
class TestBase:
    client:TestClient
    superadmin_user_credentials = LoginRequest(userName="superadmin@unittest.com",password="superadminPasswd")
    valid_user_credentials = LoginRequest(userName="admin@unittest.com",password="adminPasswd")
    invalid_user_credentials = LoginRequest(userName="invaliduser@unittest.com",password="invalid")

    def setup_super_admin(self):
        login_result = self.client.post('/login', data=self.superadmin_user_credentials.model_dump_json())
        assert login_result.status_code == 200

    def setup_class(self):
        self.client = TestClient(app)
        self.setup_super_admin(self)

    def teardown_class(self):
        pass