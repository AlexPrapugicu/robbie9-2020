from pydispatch import dispatcher

TAKE_PICTURE_SIGNAL = 'image_taken_signal'
TAKE_PICTURE_SENDER = 'image_taken_sender'

UPLOAD_IMAGE_SIGNAL = 'upload_image_signal'
UPLOAD_IMAGE_SENDER = 'upload_image_sender'

DETECT_TRAFFIC_LIGHT_SIGNAL = 'detect_traffic_light_signal'
DETECT_TRAFFIC_LIGHT_SENDER = 'detect_traffic_light_sender'

MOVE_FORWARD_SIGNAL = 'move_forward_signal'
MOVE_FORWARD_SENDER = 'move_forward_sender'


class CarEventProcessor:
    def __init__(self):
        dispatcher.connect(take_picture_dispatcher_recieve(), signal=TAKE_PICTURE_SIGNAL, sender=TAKE_PICTURE_SENDER)
        dispatcher.connect(upload_image_dispatcher_recieve(), signal=UPLOAD_IMAGE_SIGNAL, sender=UPLOAD_IMAGE_SENDER)
        dispatcher.connect(detect_traffic_light_dispatcher_recieve(), signal=DETECT_TRAFFIC_LIGHT_SIGNAL, sender=DETECT_TRAFFIC_LIGHT_SENDER)
        dispatcher.connect(move_forward_dispatcher_recieve(), signal=MOVE_FORWARD_SIGNAL, sender=MOVE_FORWARD_SENDER)


def take_picture_dispatcher_recieve(self):
    dispatcher.send(message='taking image', signal=TAKE_PICTURE_SIGNAL, sender=TAKE_PICTURE_SENDER)


def upload_image_dispatcher_recieve(self):
    dispatcher.send(message='image uploading', signal=UPLOAD_IMAGE_SIGNAL, sender=UPLOAD_IMAGE_SENDER)


def detect_traffic_light_dispatcher_recieve(self):
    dispatcher.send(message='analyzing photo', signal=DETECT_TRAFFIC_LIGHT_SIGNAL,
                    sender=DETECT_TRAFFIC_LIGHT_SENDER)


def move_forward_dispatcher_recieve(self):
    dispatcher.send(message='moving forward', signal=MOVE_FORWARD_SIGNAL, sender=MOVE_FORWARD_SENDER)
