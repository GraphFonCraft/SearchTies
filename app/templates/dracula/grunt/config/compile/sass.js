/**
 * Configuration for Sass task(s)
 */
'use strict';

var taskConfig = function(grunt) {

    grunt.config.set('sass', {
        server: {
            options: {
                precision: 10,
                style: 'nested',
                loadPath: [
                    '<%= yeogurt.client %>/styles/'
                ]
            },
            files: {
                '<%= yeogurt.staticServer %>/styles/main.css': '<%= yeogurt.client %>/styles/main.sass'
            }
        },
        dist: {
            options: {
                precision: 10,
                style: 'compressed',
                loadPath: [
                    '<%= yeogurt.client %>/styles/'
                ]
            },
            files: {
                '<%= yeogurt.dist %>/styles/main.css': '<%= yeogurt.client %>/styles/main.sass'
            }
        }
    });

};

module.exports = taskConfig;