import $ from 'jquery';
import './icon-picker';

export default class IconWidget {
    constructor (element) {
        let data = element.data();
        let name = data.name;
        let iconPicker = element.find('.js-icon-' + name + ' .js-icon-picker');
        let iconSet = element.find('.js-icon-' + name + ' .js-iconset');
        let enableIconCheckbox = element.find('.js-icon-' + name + ' .js-icon-enable');
        let widgets = element.find('.js-icon-' + name + ' .js-icon-widgets');
        let iconPickerButton = iconPicker.find('button');
        let initialValue = iconPickerButton.data('icon');
        let initialIconset = data.iconset;

        try {
            // in case custom iconset is used
            initialIconset = JSON.parse(initialIconset);
        } catch (e) {
            // ignore error for now
        }

        // initialize bootstrap iconpicker functionality
        iconPickerButton.iconpicker({
            arrowClass: 'btn-default',
            icon: initialValue,
            iconset: initialIconset,
            arrowNextIconClass: 'djangocms-icon-right',
            arrowPrevIconClass: 'djangocms-icon-left',
            inline: true,
        });

        // show label instead of dropdown if there is only one choice available
        if (iconSet.find('option').length === 1) {
            iconSet.hide();
            iconSet.parent().prepend('' +
                '<label class="form-control-static">' +
                    iconSet.find('option').text() +
                '</label>');
        }

        // set correct iconset when switching the font via dropdown
        iconSet.on('change', function () {
            let select = $(this),
                iconset = select.val(),
                selected = select.find(':selected'),
                version = selected.data('iconset-version');

            try {
                iconset = JSON.parse(iconset);
            } catch (e) {
                // ignore error for now
            }

            iconPicker.find('input[name=iconset]').val(iconset);

            iconPickerButton.iconpicker('setVersion', version);
            iconPickerButton.iconpicker('setIconset', iconset);
        });

        iconPickerButton.on('change', function() {
            const options = iconPickerButton.data('bs.iconpicker').options;
            iconPicker.children('input[name=' + data.name + ']').val(options.iconClass + ' ' + options.icon);
        });

        // checkbox is shown if field is not required, switches visibility
        // of icon selection to on/off
        enableIconCheckbox.on('change', function () {
            if ($(this).prop('checked')) {
                widgets.removeClass('hidden');
                const options = iconPickerButton.data('bs.iconpicker').options;

                if (options.icon) {
                    iconPickerButton.find('input').val(options.icon).trigger('change');
                    iconPicker.children('input[name=' + data.name + ']').val(options.iconClass + ' ' + options.icon);
                }
            } else {
                widgets.addClass('hidden');
                iconPickerButton.find('input').val('').trigger('change');
                iconPicker.children('input[name=' + data.name + ']').val('');
            }
        }).trigger('change');
    }
}
