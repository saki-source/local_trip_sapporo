$(function() {
    $('.top_logo').bgSwitcher({
        images: ['../static/img/top_photo01.jpg', '../static/img/food_photo07.png', '../static/img/rest_photo12.png','../static/img/spot_photo01.png'], // 切り替える背景画像を指定
        interval: 5000, // 背景画像を切り替える間隔を指定 3000=3秒
        loop: true, // 切り替えを繰り返すか指定 true=繰り返す false=繰り返さない
        shuffle: false, // 背景画像の順番をシャッフルするか指定 true=する false=しない
        effect: "fade", // エフェクトの種類をfade,blind,clip,slide,drop,hideから指定
        duration: 2000, // エフェクトの時間を指定します。
        easing: "swing" // エフェクトのイージングをlinear,swingから指定
    });
});