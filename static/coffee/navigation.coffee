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
			navbar_titles : $(".navbar-menu", ".header")
			titles        : $(".title", ".header")
			body_content  : $(".body")
			map           : $(".map")
		# set elements size 
		@relayout()
		# bind event
		$('body').scrollspy({ target: ".navbar-menu", offset: 170 })
		lazy_relayout = _.debounce(@relayout, 500)
		$(window).resize(lazy_relayout)
		$(window).scroll(@onFirstPageScroll); @onFirstPageScroll() if @uis.firstPage.length
		@uis.titles.on("click", (e) => @onTitleClick($(e.currentTarget).find("a").attr("href")))
		$(document).on 'heightHasChanged', => # from mosaic for instance
			$("body").each(-> $(this).scrollspy('refresh'))
			@relayout()
		# hack for z-index
		$(".header .dropdown.languages").on("show.bs.dropdown", => @uis.header.css("z-index", 3))
		$(".header .dropdown.languages").on("hide.bs.dropdown", => @uis.header.css("z-index", 1))

	relayout: =>
		window_height = $(window).height()
		window_width = $(window).width()
		if @uis.firstPage.length > 0
			@uis.firstPage.css
				height: window_height - @uis.body_content.offset().top - @uis.footer.outerHeight(true)
		# center the title links in the header
		@uis.navbar_titles.css("margin-left", 0 - @uis.navbar_titles.width() / 2)
		# map responsive
		@uis.map
			.find(".wrapper")
				.css
					"width"     : window_width
					"height"    : window_width / 3.282051282
					"font-size" : "#{Math.min(window_width/1280, 1)}em"
			.find("img")
				.css("width", window_width)

	onFirstPageScroll: =>
		scroll_top = $(window).scrollTop()
		# toggle footer
		if scroll_top == 0 then @uis.footer.removeClass("white") else @uis.footer.addClass("white")
		# toggle header
		if scroll_top > @CONFIG.headerHeight then @uis.header.removeClass("intro") else @uis.header.addClass("intro")
		if scroll_top >= $(document).height() - $(window).height() then @uis.footer.removeClass("white")

	onTitleClick: (anchor) =>
		offset = $(anchor).offset().top - (@uis.header.outerHeight(true) + @uis.header.offset().top + 50)
		$('html, body').animate({scrollTop: offset}, 'slow')
		return false

# EOF
