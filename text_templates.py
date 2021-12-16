import item as itm

line_separator = "➖➖➖➖➖➖➖➖➖➖"


# Multiple lines
def get_profile_template(chatid, user_orders, user_balance, user_reg_date):
    return f"{line_separator}\n📝 id:{chatid}\n📈 Кол-во заказов: {len(user_orders)}\n💸 Баланс: {user_balance}руб.\n📅 Дата регистрации: {user_reg_date}"

def get_faq_template(shop_name):
    return f"{line_separator}\nℹ️ FAQ магазина {shop_name}\n{line_separator}"

def get_categories_template():
    return f"{line_separator}\n🛍️ Категории\n{line_separator}"

def get_category_was_created_successfuly(cat_name):
    return f"Категория {cat_name} была успешно создана."

def get_category_data(cat):
    return f"{line_separator}\nID: {cat.get_id()}\nНазвание: {cat.get_name()}\n{line_separator}"

def get_item_card(item=None, name=None, price=None, desc=None):
    if item:
        name = item.get_name()
        price = item.get_price()
        desc = item.get_desc()
    return f"{line_separator}\n{name} - {'{:.2f}'.format(price)} руб.\n{line_separator}\n{desc}"

# Single phrases
error = "Произошла ошибка!"

# /start buttons
admin_panel = "🔴 Админ панель"
faq = "ℹ️ FAQ"
profile = "📁 Профиль"
catalogue = "🛒 Каталог"
support_menu = "☎ Меню тех. поддержки"

# Admin panel tabs
item_management = "📦 Управление товаром"
user_management = "🧍 Управление пользователями"
shop_stats = "📈 Статистика магазина (BETA)"
bot_settings = "⚙ Настройки бота"

# Profile buttons
my_orders = "📂 Мои заказы"
my_support_tickets = "🙋 Мои тикеты в тех. поддержку"
enable_notif = "🔔Включить ововещения о кол-ве товара"
disable_notif = "🔕Выключить ововещения о кол-ве товара"

# Item management
add_cat = "🛍️Добавить категорию"
add_item = "🗃️Добавить товар"
change_cat = "✏️ Изменить категорию"
change_item = "✏️ Изменить товар"

# User management
user_profile = "📁Профиль пользователя"
notify_everyone = "🔔Оповещение всем пользователям"

# Shop stats
registration_stats = "👥Статистика регистраций"
order_stats = "📦Статистика заказов"

# Shop settings
main_settings = "🛠️Основные настройки"
stats_settings = "📈Настройки статистики"

# Misc buttons
back = "🔙 Назад"
confirm = "✅ Да"
deny = "❌ Нет"