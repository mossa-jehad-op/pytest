import pytest
from unittest.mock import MagicMock
from day16 import get_post_by_id, get_posts_by_user_id, get_post_by_id_with_validation

BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

def test_get_post_by_id(mocker):
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = {'id': 1, 'title': 'Test Post'}
    mock_response.raise_for_status = MagicMock()
    mocker.patch('day16.http_get', return_value=mock_response)

    result = get_post_by_id(1)
    assert result == {'id': 1, 'title': 'Test Post'}

def test_get_posts_by_user_id(mocker):
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = [{'id': 1, 'userId': 1, 'title': 'User Post'}]
    mock_response.raise_for_status = MagicMock()
    mocker.patch('day16.http_get', return_value=mock_response)

    result = get_posts_by_user_id(1)
    assert result == [{'id': 1, 'userId': 1, 'title': 'User Post'}]

def test_get_post_by_id_with_validation(mocker):
    mock_response = mocker.MagicMock()
    mock_response.json.return_value = {'id': 1, 'title': 'Validated Post'}
    mock_response.raise_for_status = MagicMock()
    mocker.patch('day16.http_get', return_value=mock_response)

    result = get_post_by_id_with_validation(1)
    assert result == {'id': 1, 'title': 'Validated Post'}

def test_get_post_by_id_with_validation_error():
    with pytest.raises(ValueError, match='post_id must be greater than 0'):
        get_post_by_id_with_validation(0)
