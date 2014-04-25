#!/usr/bin/coffee
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 24-Apr-2014
# Last mod : 24-Apr-2014
# -----------------------------------------------------------------------------

class window.Navigation

	constructor: ->
		@uis =
			firstPage : $(".first-page")
		# set elements size 
		@relayout()
		# bind event
		$('body').scrollspy({ target: '.navbar-title', offset: 50 })
		$(window).resize(@relayout)
		$(document).on 'heighHasChanged', -> # from mosaic for instance
			$("body").each(-> $(this).scrollspy('refresh'))

	relayout: =>
		window_height = $(window).height()
		if @uis.firstPage.length > 0
			@uis.firstPage.css
				height: window_height - @uis.firstPage.offset().top

# EOF
