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
# Last mod : 29-Apr-2014
# -----------------------------------------------------------------------------

class window.Navigation

	constructor: ->
		@CONFIG = 
			headerHeight : 70
		@uis =
			firstPage     : $(".first-page")
			footer        : $(".footer")
			header        : $(".header")
			navbar_titles : $(".navbar-title", ".header")
			body_content  : $(".body")
		# set elements size 
		@relayout()
		# bind event
		$('body').scrollspy({ target: ".navbar-title", offset: @CONFIG.headerHeight })
		lazy_relayout = _.debounce(@relayout, 500)
		$(window).resize(lazy_relayout)
		$(window).scroll(@onFirstPageScroll); @onFirstPageScroll() if @uis.firstPage.length
		$(document).on 'heightHasChanged', => # from mosaic for instance
			$("body").each(-> $(this).scrollspy('refresh'))
			@relayout()
		# hack for z-index
		$(".header .dropdown.languages").on("show.bs.dropdown", => @uis.header.css("z-index", 3))
		$(".header .dropdown.languages").on("hide.bs.dropdown", => @uis.header.css("z-index", 1))

	relayout: =>
		window_height = $(window).height()
		if @uis.firstPage.length > 0
			@uis.firstPage.css
				height: window_height - @uis.body_content.offset().top - @uis.footer.outerHeight(true)
		# center the title links in the header
		@uis.navbar_titles.css("margin-left", 0 - @uis.navbar_titles.width() / 2)

	onFirstPageScroll: =>
		scroll_top = $(window).scrollTop()
		# toggle footer
		if scroll_top == 0 then @uis.footer.removeClass("white") else @uis.footer.addClass("white")
		# toggle header
		if scroll_top > @CONFIG.headerHeight then @uis.header.removeClass("intro") else @uis.header.addClass("intro")

# EOF
