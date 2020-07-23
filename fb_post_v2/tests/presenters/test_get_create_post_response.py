from fb_post_v2.presenters import PresenterImplementation


def test_get_create_post_response():

    # Arrange
    post_id = 1
    expected_post_id_dict = {
        "post_id": post_id
    }

    json_presenter = PresenterImplementation()

    # Act
    actual_post_id = json_presenter.get_create_post_response(post_id=post_id)

    # Assert
    assert actual_post_id == expected_post_id_dict