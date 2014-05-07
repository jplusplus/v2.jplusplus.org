#!/usr/bin/coffee
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 04-May-2014
# Last mod : 04-May-2014
# -----------------------------------------------------------------------------
window.jplusplus = {} if not window.jplusplus

class window.jplusplus.ContactForm

	constructor: (scope) ->
		@ui  = $(scope)
		@uis =
			form           : $("form", @ui)
			successMessage : $(".success-message", @ui)
			backToFormBtn  : $(".success-message a", @ui)
			submitBtn      : $('.nl-submit', @ui)

		new NLForm(@uis.form.get(0))
		# bind event
		@uis.submitBtn.on("click", @onSubmitClick)
		@uis.backToFormBtn.on("click", @backToForm)

	onSubmitClick: (e) =>
		data = @uis.form.serialize()
		$.ajax
			url      : @uis.form.attr("action")
			type     : "post"
			data     : data
			success  : =>
				# fix he height of the element before removing content
				@ui.css('min-height', @ui.outerHeight(true))
				@uis.successMessage.removeClass("hidden")
				@uis.form.addClass("hidden")
		# prevent the page reload
		e.preventDefault()
		return false

	backToForm: (e) =>
		# reset dynamic height
		@ui.css('min-height', '')
		@uis.successMessage.addClass("hidden")
		@uis.form.removeClass("hidden")
		e.preventDefault()
		return false

# EOF
