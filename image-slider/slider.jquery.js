(function ($) {
    $.fn.slider = function (options) {
        var defaults = {duration: 1000};
        var settings = $.extend({}, defaults, options);

        return this.each(function () {
            const $slider = $(this);
            const $sliderList = $slider.children("ul");
            let $sliderItems = $sliderList.children("li");
            const $buttons = $(".button");

            const width = getImageWidth();
            const count = $sliderItems.length;
            const marginLeftStart = 0;
            const marginLeftEnd = -(width * (count - 1));

            $buttons.on("click", function (event) {
                event.preventDefault();
                const marginLeft = getMarginLeft();
                const isBack = $(this).hasClass("back");
                const duration = settings.duration;
                let direction = null;

                if (isBack) {
                    if (_atStart()) {
                        // TODO: 效率需要改进
                        // 添加一个伪首部（复制原尾部）、伪尾部（复制原首部）
                        $sliderList.prepend($sliderItems.last());
                        $sliderItems = $sliderList.children("li");
                        animateSliderDirection("-", 0);
                    }
                    direction = "+";
                } else {
                    if (_atEnd()) {
                        $sliderList.append($sliderItems.first());
                        $sliderItems = $sliderList.children("li");
                        animateSliderDirection("+", 0);
                    }
                    direction = "-";
                }
                animateSliderDirection(direction, duration);

                function _atStart() {
                    return marginLeft > -width && marginLeft <= marginLeftStart;
                }

                function _atEnd() {
                    return marginLeft >= marginLeftEnd &&
                        marginLeft < -(width * (count - 2));
                }

                function getMarginLeft() {
                    return parseInt($sliderList.css("margin-left"), 10);
                }
            });


            function animateSliderToStart(duration) {
                animateSliderMargin(marginLeftStart, duration);
            }

            function animateSliderToEnd(duration) {
                animateSliderMargin(marginLeftEnd, duration);
            }

            function animateSliderDirection(direction, duration) {
                if (direction !== "+" && direction !== "-") {
                    throw Error("direction must be '+' or '-'");
                }
                animateSliderMargin(direction + "=" + width + "px", duration);
            }

            function animateSliderMargin(marginLeft, duration) {
                console.log(marginLeft);
                $sliderList.finish().animate({
                    "margin-left": marginLeft
                }, duration);
            }

            function getImageWidth() {
                return $sliderItems.first().width();
            }
        });
    };
})(jQuery);