document.addEventListener("DOMContentLoaded", function () {
    // 1) Проверка, есть ли форма (валидация)
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function (event) {
            let phoneInput = document.querySelector("input[name='phone']");
            let emailInput = document.querySelector("input[name='email']");
            let passwordInput = document.querySelector("input[name='password']");

            if (!phoneInput.value.match(/^\d{10,15}$/)) {
                alert("Введите корректный номер телефона (от 10 до 15 цифр)!");
                event.preventDefault();
            }
            if (!emailInput.value.includes("@")) {
                alert("Введите корректный email!");
                event.preventDefault();
            }
            if (passwordInput.value.length < 6) {
                alert("Пароль должен содержать минимум 6 символов!");
                event.preventDefault();
            }
        });
    }
});
document.addEventListener("DOMContentLoaded", function () {

    // 1. ВЫПАДАЮЩЕЕ МЕНЮ ДЛЯ МОБИЛЬНЫХ
    const dropdowns = document.querySelectorAll(".dropdown");
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener("click", function (event) {
            event.stopPropagation();
            this.classList.toggle("active");
        });
    });

    // Закрытие выпадающего меню при клике вне его
    document.addEventListener("click", function () {
        dropdowns.forEach(dropdown => dropdown.classList.remove("active"));
    });


    // 3. ЛЕНИВАЯ ЗАГРУЗКА ИЗОБРАЖЕНИЙ
    const lazyImages = document.querySelectorAll("img");
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                observer.unobserve(img);
            }
        });
    });

    lazyImages.forEach(img => imageObserver.observe(img));

    // 4. ПЛАВНЫЙ СКРОЛЛ ПО ЯКОРЯМ
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 50,
                    behavior: "smooth"
                });
            }
        });
    });

    // 5. ПОЯВЛЕНИЕ КОНТЕНТА ПРИ ПРОКРУТКЕ
    const fadeElements = document.querySelectorAll(".content, .two-column-section");

    const fadeInObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    fadeElements.forEach(element => {
        element.style.opacity = "0";
        element.style.transform = "translateY(30px)";
        element.style.transition = "opacity 1s ease-out, transform 1s ease-out";
        fadeInObserver.observe(element);
    });

});


/*******************************************
 * 1) Функция для чтения куки: getCookie
 *******************************************/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Извлекаем CSRF-токен:
const csrftoken = getCookie('csrftoken');

/*******************************************
 * 2) Логика заполнения списка моделей
 *******************************************/
const carOptions = {
  sedan: ["Velocity Prime", "Astra Nova", "Echelon Drive"],
  suv: ["Mountain Hawk d", "Tundra Pro", "Northern Wind"],
  coupe: ["Luxe Horizon", "Ignis Edge", "Stellar Curve"],
  premium: ["Regal Voyage", "Prestige Line", "Elite Sphere"]
};

document.addEventListener("DOMContentLoaded", function() {
    const carBodySelect = document.getElementById("car-body-type");
    const carModelSelect = document.getElementById("car-model");

    if (carBodySelect && carModelSelect) {
        carBodySelect.addEventListener("change", function() {
            carModelSelect.innerHTML = "";
            const selectedBody = this.value;
            if (selectedBody && carOptions[selectedBody]) {
                carOptions[selectedBody].forEach(model => {
                    const option = document.createElement("option");
                    option.value = model;
                    option.textContent = model;
                    carModelSelect.appendChild(option);
                });
            } else {
                const placeholderOption = document.createElement("option");
                placeholderOption.value = "";
                placeholderOption.textContent = "Сначала выберите тип кузова";
                carModelSelect.appendChild(placeholderOption);
            }
        });
    }
});

/*******************************************
 * 3) Логика отправки формы Fetch (POST)
 *******************************************/
document.addEventListener("DOMContentLoaded", function() {
    const orderForm = document.getElementById("orderForm");
    if (orderForm) {
        orderForm.addEventListener("submit", function(event) {
            event.preventDefault(); // отменяем обычную отправку формы

            // Собираем данные из формы
            const formData = {
                first_name: document.getElementById("firstName").value,
                last_name: document.getElementById("lastName").value,
                phone: document.getElementById("phone").value,
                car_body_type: document.getElementById("car-body-type").value,
                car_model: document.getElementById("car-model").value
            };

            // Выполняем POST-запрос
            fetch("/api/orders/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken   // <-- Критически важно для Django
                },
                body: JSON.stringify(formData)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Ошибка при отправке заказа");
                }
                return response.json();
            })
            .then(data => {
                alert(`Заказ создан!Протягом дня з вами зв'яжеться менеджер Олександр для уточнення всіх деталей. Номер заказа: ${data.id}`);
                // Сбрасываем форму
                orderForm.reset();
            })
            .catch(error => {
                console.error(error);
                alert("Произошла ошибка. Попробуйте ещё раз!");
            });
        });
    }
});



