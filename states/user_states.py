from aiogram.dispatcher.filters.state import StatesGroup, State


class UserForms(StatesGroup):
    full_name = State()
    phone = State()


class UserBuy(StatesGroup):
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


class UserProfile(StatesGroup):
    edit_name = State()
    edit_phone = State()
    edit_username = State()


class UserFeedback(StatesGroup):
    photo = State()
    photo_text = State()
    text = State()


class UserCars(StatesGroup):
    main = State()
    first = State()


class LogisticAsia(StatesGroup):
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


class LogisticCIS(StatesGroup):
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


class LogisticChina(StatesGroup):
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


class LogisticUSA(StatesGroup):
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


class LogisticEurope(StatesGroup):
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()
    seven = State()
    eight = State()
    nine = State()
