/**
 * Configuration for Jade task(s)
 */
'use strict';

var taskConfig = function(grunt) {

	var data = JSON.parse(require('fs').readFileSync('./locals.json', 'utf8'));
	data.package = JSON.parse(require('fs').readFileSync('./package.json', 'utf8'));

    grunt.config.set('jade', {
        server: {
            options: {
                pretty: true,
                client: false,
                data: function(dest, src){
	                data.debug = true;
					return data
                }
            },
            expand: true,
            cwd: '<%= yeogurt.client %>/templates/',
            dest: '<%= yeogurt.staticServer %>/',
            src: ['*.jade'],
            ext: '.html'
        },
        dist: {
            options: {
                pretty: true,
                client: false,
                data: function(dest, src){
	                data.debug = false;
					return data
                }
            },
            expand: true,
            cwd: '<%= yeogurt.client %>/templates/',
            dest: '<%= yeogurt.dist %>/',
            src: ['*.jade'],
            ext: '.html'
        },
    });

};

module.exports = taskConfig;
