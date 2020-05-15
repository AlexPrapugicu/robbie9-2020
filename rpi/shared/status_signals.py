class StatusSignals:
    def __init__(self):
        self.TAKE_PICTURE_SIGNAL = 'image_taken_signal'
        self.TAKE_PICTURE_SENDER = 'image_taken_sender'

        self.UPLOAD_IMAGE_SIGNAL = 'upload_image_signal'
        self.UPLOAD_IMAGE_SENDER = 'upload_image_sender'

        self.TRAFFIC_LIGHT_DETECTED_SIGNAL = 'detect_traffic_light_signal'
        self.TRAFFIC_LIGHT_DETECTED_SENDER = 'detect_traffic_light_sender'

        self.TRAFFIC_LIGHT_NOT_PRESENT_SIGNAL = 'no_traffic_light_signal'
        self.TRAFFIC_LIGHT_NOT_PRESENT_SENDER = 'no_traffic_light_sender'

        self.MOVE_FORWARD_SIGNAL = 'move_forward_signal'
        self.MOVE_FORWARD_SENDER = 'move_forward_sender'

        self.RUNNING_SIGNAL = 'running_signal'
        self.RUNNING_SENDER = 'running_sender'

        self.STOPPED_SIGNAL = 'stopped_signal'
        self.STOPPED_SENDER = 'stopped_sender'

        self.IMAGE_UPLOADED_SIGNAL = 'image_uploaded_signal'
        self.IMAGE_UPLOADED_SENDER = 'image_uploaded_sender'

        self.ANALYZE_IMAGE_SIGNAL = 'analyze_image_signal'
        self.ANALYZE_IMAGE_SENDER = 'analyze_image_sender'
