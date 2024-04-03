<?php
// Создаем массив с данными об опыте работы
$experience = array(
    array(
        "jobTitle" => "Senior Developer",
        "company" => "Company A",
        "years" => "2018-2022",
    ),
    array(
        "jobTitle" => "Junior Developer",
        "company" => "Company B",
        "years" => "2015-2018",
    ),
    // Добавьте больше элементов по мере необходимости
);

// Выводим данные массива в HTML-шаблоне
foreach ($experience as $job) {
    echo "<h2>" . $job["jobTitle"] . "</h2>";
    echo "<p>Company: " . $job["company"] . "</p>";
    echo "<p>Years: " . $job["years"] . "</p>";
    echo "<hr>";
}
?>
<?php
// Создаем массив с данными об опыте работы
$experience = array(
    array(
        "jobTitle" => "Senior Developer",
        "company" => "Company A",
        "years" => "2018-2022",
    ),
    array(
        "jobTitle" => "Junior Developer",
        "company" => "Company B",
        "years" => "2015-2018",
    ),
    // Добавьте больше элементов по мере необходимости
);

// Выводим данные массива в HTML-шаблоне
foreach ($experience as $job) {
    echo "<h2>" . $job["jobTitle"] . "</h2>";
    echo "<p>Company: " . $job["company"] . "</p>";
    echo "<p>Years: " . $job["years"] . "</p>";
    echo "<hr>";
}
?>
