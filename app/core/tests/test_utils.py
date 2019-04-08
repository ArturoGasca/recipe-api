from unittest.mock import patch

from django.test import TestCase

from core import utils


class UtilsTests(TestCase):
    """Test utils functions"""

    @patch('uuid.uuid4')
    def test_recipe_file_name(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = utils.recipe_image_file_path(None, 'myimage.jpg')

        expected_path = f'uploads/recipes/{uuid}.jpg'
        self.assertEqual(file_path, expected_path)
