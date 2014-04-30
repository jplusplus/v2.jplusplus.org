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
		that = this
		@CONFIG = 
			headerHeight  : 70
			offsetScroll  : 50
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
		$('body').scrollspy({ target: ".navbar-menu", offset: @CONFIG.offsetScroll + @uis.header.offset().top +  @CONFIG.headerHeight })
		lazy_relayout = _.debounce(@relayout, 500)
		$(window).resize(lazy_relayout)
		if @uis.firstPage.length > 0
			(window).scroll(@onFirstPageScroll)
			@onFirstPageScroll() 
		$(document).on('heightHasChanged', @relayout) # from mosaic for instance
		# $("a[href^=#]").on("click", (e) -> that.onTitleClick($(this).attr("href").split("&")[0]))
		@uis.titles.on("click", (e) -> that.onTitleClick($(this).find("a").attr("href").split("&")[0]))
		# hack for z-index
		$(".header .dropdown.languages")
			.on("show.bs.dropdown", => @uis.header.css("z-index", 3))
			.on("hide.bs.dropdown", => @uis.header.css("z-index", 2))

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
					"height"    : window_width / 3.282051282 # ratio of map picture
					"font-size" : "#{Math.min(window_width/1280, 1)}em"
			.find("img")
				.css("width", window_width)
		# refresh scrollspy
		setTimeout(->
			$("body").each(-> $(this).scrollspy('refresh'))
		, 500) # because of height animation (on first-page for instance)

	onFirstPageScroll: =>
		scroll_top = $(window).scrollTop()
		# toggle footer
		if scroll_top == 0 then @uis.footer.removeClass("white") else @uis.footer.addClass("white")
		# toggle header
		if scroll_top > @CONFIG.headerHeight then @uis.header.removeClass("intro") else @uis.header.addClass("intro")
		if scroll_top >= $(document).height() - $(window).height() then @uis.footer.removeClass("white")

	onTitleClick: (anchor) =>
		offset = $(anchor).offset().top - (@CONFIG.headerHeight + @uis.header.offset().top - @CONFIG.offsetScroll)
		$('html, body').animate({scrollTop: offset}, 'slow')
		return false

# EOF
