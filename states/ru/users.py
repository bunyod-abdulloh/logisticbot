from aiogram.dispatcher.filters.state import StatesGroup, State


class UserBuyRu(StatesGroup):
    equipment = State()
    equipment_photo = State()
    equipment_comment = State()
    equipment_text = State()
    raw = State()
    raw_photo = State()
    raw_comment = State()
    raw_text = State()
    small_equipment = State()
    small_equipment_photo = State()
    small_equipment_comment = State()
    small_equipment_text = State()


class UserCarsRu(StatesGroup):
    main = State()
    first = State()


class UserFeedbackRu(StatesGroup):
    photo = State()
    photo_text = State()
    text = State()


class UserFormsRu(StatesGroup):
    full_name = State()
    phone = State()


class LogisticAsiaRu(StatesGroup):
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()
    seven = State()
    eight = State()
    nine = State()
    ten = State()


class LogisticChinaRu(StatesGroup):
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()
    seven = State()
    eight = State()
    nine = State()
    ten = State()


class LogisticCISRu(StatesGroup):
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()
    seven = State()
    eight = State()
    nine = State()
    ten = State()


class LogisticEuropeRu(StatesGroup):
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()
    seven = State()
    eight = State()
    nine = State()


class UserProfileRu(StatesGroup):
    edit_name = State()
    edit_phone = State()
    edit_username = State()


class LogisticUSARu(StatesGroup):
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()
    seven = State()
    eight = State()
    nine = State()
    ten = State()
