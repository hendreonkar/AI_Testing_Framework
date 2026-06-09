import pytest


def test_create_get_delete_booking(client, booking_payload, auth_token):
    # Create
    create_resp = client.create_booking(booking_payload)
    assert create_resp.status_code == 200
    create_data = create_resp.json()
    booking_id = create_data.get('bookingid')
    assert booking_id is not None

    # Get
    get_resp = client.get_booking(booking_id)
    assert get_resp.status_code == 200
    get_data = get_resp.json()
    assert get_data['firstname'] == booking_payload['firstname']
    assert get_data['lastname'] == booking_payload['lastname']

    # Delete
    del_resp = client.delete_booking(booking_id, auth_token)
    assert del_resp.status_code in (201, 200)

    # Verify deletion
    get_after = client.get_booking(booking_id)
    assert get_after.status_code == 404


def test_update_booking_put(client, booking_payload, auth_token):
    # Create
    create_resp = client.create_booking(booking_payload)
    assert create_resp.status_code == 200
    booking_id = create_resp.json().get('bookingid')

    # Update
    updated = booking_payload.copy()
    updated['firstname'] = 'Updated'
    put_resp = client.update_booking(booking_id, updated, auth_token)
    assert put_resp.status_code == 200
    put_data = put_resp.json()
    assert put_data['firstname'] == 'Updated'

    # Cleanup
    client.delete_booking(booking_id, auth_token)


def test_partial_update_booking_patch(client, booking_payload, auth_token):
    create_resp = client.create_booking(booking_payload)
    booking_id = create_resp.json().get('bookingid')

    patch_payload = {"firstname": "Patched"}
    patch_resp = client.partial_update_booking(booking_id, patch_payload, auth_token)
    assert patch_resp.status_code == 200
    assert patch_resp.json()['firstname'] == 'Patched'

    client.delete_booking(booking_id, auth_token)
