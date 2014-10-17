/**
 * Configuration for injector task(s)
 */
'use strict';

var _str = require('underscore.string');

var taskConfig = function(grunt) {

    grunt.config.set('injector', {
        options: {

        },
        // Inject application script files into index.html (doesn't include bower)
        jade: {
            options: {
                transform: function(filePath) {
                    filePath = filePath.replace('/client/templates/', '../');
                    return 'include ' + filePath;
                },
                starttag: '//- [injector:jade]',
                endtag: '//- [endinjector]'
            },
            files: {
                '<%= yeogurt.client %>/templates/layouts/base.jade': [
                    '<%= yeogurt.client %>/templates/**/*.jade',
                    '!<%= yeogurt.client %>/templates/*.jade',
                    '!<%= yeogurt.client %>/templates/layouts/**/*.jade',
                ]
            }
        },
        // Inject application script files into index.html (doesn't include bower)
        scripts: {
            options: {
                transform: function(filePath) {
                    filePath = filePath.replace('/client/', '');
                    return '<script src="' + filePath + '"></script>';
                },
                starttag: '// [injector:js]',
                endtag: '// [endinjector]'
            },
            files: {
                '<%= yeogurt.client %>/templates/layouts/base.jade': [
                    '<%= yeogurt.client %>/scripts/**/*.js',
                    '!<%= yeogurt.client %>/scripts/app.js'
                ]
            }
        },
        // Inject component scss into main.scss
        sass: {
            options: {
                transform: function(filePath) {
                    filePath = filePath.replace('/client/styles/', '');

                    return '@import ' + filePath.slice(0, -5);
                },
                starttag: '// [injector]',
                endtag: '// [endinjector]'
            },
            files: {
                '<%= yeogurt.client %>/styles/main.sass': [
                    '<%= yeogurt.client %>/styles/**/*.sass',
					'!<%= yeogurt.client %>/styles/_*/**/*.sass',
                    '!<%= yeogurt.client %>/styles/_index.sass',
                    '!<%= yeogurt.client %>/styles/main.sass'
                ]
            }
        },
        // Inject component css into index.html
        css: {
            options: {
                transform: function(filePath) {
                    filePath = filePath.replace('/client/', '');
                    return 'link(rel=\'stylesheet\', href=\'' + filePath + '\')';
                },
                starttag: '// [injector:css]',
                endtag: '// [endinjector]'
            },
            files: {
                '<%= yeogurt.client %>/templates/layouts/base.jade': [
                    '<%= yeogurt.client %>/styles/**/*.css',
                    '!<%= yeogurt.client %>/styles/main.css'
                ]
            }
        }
    });

};

module.exports = taskConfig;
