# Андрей Нацевич, 43-я когорта — Финальный проект. Инженер по тестированию / QA
import sender_stand_request
import data

def test_create_and_get_order_by_track_success():
    # Шаг 1: Выполнить запрос на создание заказа
    response = sender_stand_request.post_new_order(data.order_body)
    
    # Шаг 2: Сохранить номер трека заказа из ответа
    track_number = response.json()["track"]
    
    # Шаг 3: Выполнить запрос на получение заказа по треку
    get_order_response = sender_stand_request.get_order_by_track(track_number)
    
    # Шаг 4: Проверить, что код ответа равен 200
    assert get_order_response.status_code == 200