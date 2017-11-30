import $ from 'jquery';
import IconWidget from './icon-widget';

$(() => {
    const widgets = $('.djangocms-icon');

    if (widgets.length) {
        widgets.each(function () {
            new IconWidget($(this));
        });

        window.djangoCMSIcon = {
            widgets,
            $
        }
    }
});
