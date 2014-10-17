/**
 * Configuration for Sass task(s)
 */
'use strict';

var taskConfig = function(grunt) {

    grunt.config.set('sass', {
        server: {
            options: {
                precision: 10,
                outputStyle: 'nested',
                sourceMap: true,
                includePaths: [
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
                outputStyle: 'compressed',
                sourceMap: true,
                includePaths: [
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
