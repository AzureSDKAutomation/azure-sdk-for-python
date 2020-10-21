# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class CustomInstanceOperations(object):
    """CustomInstanceOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar x_bing_apis_sdk: Activate swagger compliance. Constant value: "true".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config
        self.x_bing_apis_sdk = "true"

    def image_search(
            self, custom_config, query, accept_language=None, user_agent=None, client_id=None, client_ip=None, location=None, aspect=None, color=None, country_code=None, count=None, freshness=None, height=None, id=None, image_content=None, image_type=None, license=None, market=None, max_file_size=None, max_height=None, max_width=None, min_file_size=None, min_height=None, min_width=None, offset=None, safe_search=None, size=None, set_lang=None, width=None, custom_headers=None, raw=False, **operation_config):
        """The Custom Image Search API lets you send an image search query to Bing
        and get image results found in your custom view of the web.

        :param custom_config: The identifier for the custom search
         configuration
        :type custom_config: str
        :param query: The user's search query term. The term cannot be empty.
         The term may contain [Bing Advanced
         Operators](http://msdn.microsoft.com/library/ff795620.aspx). For
         example, to limit images to a specific domain, use the
         [site:](http://msdn.microsoft.com/library/ff795613.aspx) operator. To
         help improve relevance of an insights query (see
         [insightsToken](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)),
         you should always include the user's query term. Use this parameter
         only with the Image Search API.Do not specify this parameter when
         calling the Trending Images API.
        :type query: str
        :param accept_language: A comma-delimited list of one or more
         languages to use for user interface strings. The list is in decreasing
         order of preference. For additional information, including expected
         format, see
         [RFC2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
         This header and the
         [setLang](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         query parameter are mutually exclusive; do not specify both. If you
         set this header, you must also specify the
         [cc](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         query parameter. To determine the market to return results for, Bing
         uses the first supported language it finds from the list and combines
         it with the cc parameter value. If the list does not include a
         supported language, Bing finds the closest language and market that
         supports the request or it uses an aggregated or default market for
         the results. To determine the market that Bing used, see the
         BingAPIs-Market header. Use this header and the cc query parameter
         only if you specify multiple languages. Otherwise, use the
         [mkt](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         and
         [setLang](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         query parameters. A user interface string is a string that's used as a
         label in a user interface. There are few user interface strings in the
         JSON response objects. Any links to Bing.com properties in the
         response objects apply the specified language.
        :type accept_language: str
        :param user_agent: The user agent originating the request. Bing uses
         the user agent to provide mobile users with an optimized experience.
         Although optional, you are encouraged to always specify this header.
         The user-agent should be the same string that any commonly used
         browser sends. For information about user agents, see [RFC
         2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html). The
         following are examples of user-agent strings. Windows Phone:
         Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0;
         IEMobile/10.0; ARM; Touch; NOKIA; Lumia 822). Android: Mozilla / 5.0
         (Linux; U; Android 2.3.5; en - us; SCH - I500 Build / GINGERBREAD)
         AppleWebKit / 533.1 (KHTML; like Gecko) Version / 4.0 Mobile Safari /
         533.1. iPhone: Mozilla / 5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X)
         AppleWebKit / 536.26 (KHTML; like Gecko) Mobile / 10B142 iPhone4; 1
         BingWeb / 3.03.1428.20120423. PC: Mozilla / 5.0 (Windows NT 6.3;
         WOW64; Trident / 7.0; Touch; rv:11.0) like Gecko. iPad: Mozilla / 5.0
         (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit / 537.51.1 (KHTML, like
         Gecko) Version / 7.0 Mobile / 11A465 Safari / 9537.53
        :type user_agent: str
        :param client_id: Bing uses this header to provide users with
         consistent behavior across Bing API calls. Bing often flights new
         features and improvements, and it uses the client ID as a key for
         assigning traffic on different flights. If you do not use the same
         client ID for a user across multiple requests, then Bing may assign
         the user to multiple conflicting flights. Being assigned to multiple
         conflicting flights can lead to an inconsistent user experience. For
         example, if the second request has a different flight assignment than
         the first, the experience may be unexpected. Also, Bing can use the
         client ID to tailor web results to that client ID’s search history,
         providing a richer experience for the user. Bing also uses this header
         to help improve result rankings by analyzing the activity generated by
         a client ID. The relevance improvements help with better quality of
         results delivered by Bing APIs and in turn enables higher
         click-through rates for the API consumer. IMPORTANT: Although
         optional, you should consider this header required. Persisting the
         client ID across multiple requests for the same end user and device
         combination enables 1) the API consumer to receive a consistent user
         experience, and 2) higher click-through rates via better quality of
         results from the Bing APIs. Each user that uses your application on
         the device must have a unique, Bing generated client ID. If you do not
         include this header in the request, Bing generates an ID and returns
         it in the X-MSEdge-ClientID response header. The only time that you
         should NOT include this header in a request is the first time the user
         uses your app on that device. Use the client ID for each Bing API
         request that your app makes for this user on the device. Persist the
         client ID. To persist the ID in a browser app, use a persistent HTTP
         cookie to ensure the ID is used across all sessions. Do not use a
         session cookie. For other apps such as mobile apps, use the device's
         persistent storage to persist the ID. The next time the user uses your
         app on that device, get the client ID that you persisted. Bing
         responses may or may not include this header. If the response includes
         this header, capture the client ID and use it for all subsequent Bing
         requests for the user on that device. If you include the
         X-MSEdge-ClientID, you must not include cookies in the request.
        :type client_id: str
        :param client_ip: The IPv4 or IPv6 address of the client device. The
         IP address is used to discover the user's location. Bing uses the
         location information to determine safe search behavior. Although
         optional, you are encouraged to always specify this header and the
         X-Search-Location header. Do not obfuscate the address (for example,
         by changing the last octet to 0). Obfuscating the address results in
         the location not being anywhere near the device's actual location,
         which may result in Bing serving erroneous results.
        :type client_ip: str
        :param location: A semicolon-delimited list of key/value pairs that
         describe the client's geographical location. Bing uses the location
         information to determine safe search behavior and to return relevant
         local content. Specify the key/value pair as <key>:<value>. The
         following are the keys that you use to specify the user's location.
         lat (required): The latitude of the client's location, in degrees. The
         latitude must be greater than or equal to -90.0 and less than or equal
         to +90.0. Negative values indicate southern latitudes and positive
         values indicate northern latitudes. long (required): The longitude of
         the client's location, in degrees. The longitude must be greater than
         or equal to -180.0 and less than or equal to +180.0. Negative values
         indicate western longitudes and positive values indicate eastern
         longitudes. re (required): The radius, in meters, which specifies the
         horizontal accuracy of the coordinates. Pass the value returned by the
         device's location service. Typical values might be 22m for GPS/Wi-Fi,
         380m for cell tower triangulation, and 18,000m for reverse IP lookup.
         ts (optional): The UTC UNIX timestamp of when the client was at the
         location. (The UNIX timestamp is the number of seconds since January
         1, 1970.) head (optional): The client's relative heading or direction
         of travel. Specify the direction of travel as degrees from 0 through
         360, counting clockwise relative to true north. Specify this key only
         if the sp key is nonzero. sp (optional): The horizontal velocity
         (speed), in meters per second, that the client device is traveling.
         alt (optional): The altitude of the client device, in meters. are
         (optional): The radius, in meters, that specifies the vertical
         accuracy of the coordinates. Specify this key only if you specify the
         alt key. Although many of the keys are optional, the more information
         that you provide, the more accurate the location results are. Although
         optional, you are encouraged to always specify the user's geographical
         location. Providing the location is especially important if the
         client's IP address does not accurately reflect the user's physical
         location (for example, if the client uses VPN). For optimal results,
         you should include this header and the X-MSEdge-ClientIP header, but
         at a minimum, you should include this header.
        :type location: str
        :param aspect: Filter images by the following aspect ratios. All: Do
         not filter by aspect.Specifying this value is the same as not
         specifying the aspect parameter. Square: Return images with standard
         aspect ratio. Wide: Return images with wide screen aspect ratio. Tall:
         Return images with tall aspect ratio. Possible values include: 'All',
         'Square', 'Wide', 'Tall'
        :type aspect: str or
         ~azure.bing.search.customimagesearch.models.ImageAspect
        :param color: Filter images by the following color options. ColorOnly:
         Return color images. Monochrome: Return black and white images. Return
         images with one of the following dominant colors: Black, Blue, Brown,
         Gray, Green, Orange, Pink, Purple, Red, Teal, White, Yellow. Possible
         values include: 'ColorOnly', 'Monochrome', 'Black', 'Blue', 'Brown',
         'Gray', 'Green', 'Orange', 'Pink', 'Purple', 'Red', 'Teal', 'White',
         'Yellow'
        :type color: str or
         ~azure.bing.search.customimagesearch.models.ImageColor
        :param country_code: A 2-character country code of the country where
         the results come from. For a list of possible values, see [Market
         Codes](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview).
         If you set this parameter, you must also specify the
         [Accept-Language](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         header. Bing uses the first supported language it finds from the
         languages list, and combine that language with the country code that
         you specify to determine the market to return results for. If the
         languages list does not include a supported language, Bing finds the
         closest language and market that supports the request, or it may use
         an aggregated or default market for the results instead of a specified
         one. You should use this query parameter and the Accept-Language query
         parameter only if you specify multiple languages; otherwise, you
         should use the mkt and setLang query parameters. This parameter and
         the
         [mkt](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         query parameter are mutually exclusive—do not specify both.
        :type country_code: str
        :param count: The number of images to return in the response. The
         actual number delivered may be less than requested. The default is 35.
         The maximum value is 150. You use this parameter along with the offset
         parameter to page results.For example, if your user interface displays
         20 images per page, set count to 20 and offset to 0 to get the first
         page of results.For each subsequent page, increment offset by 20 (for
         example, 0, 20, 40). Use this parameter only with the Image Search
         API.Do not specify this parameter when calling the Insights, Trending
         Images, or Web Search APIs.
        :type count: int
        :param freshness: Filter images by the following discovery options.
         Day: Return images discovered by Bing within the last 24 hours. Week:
         Return images discovered by Bing within the last 7 days. Month: Return
         images discovered by Bing within the last 30 days. Possible values
         include: 'Day', 'Week', 'Month'
        :type freshness: str or
         ~azure.bing.search.customimagesearch.models.Freshness
        :param height: Filter images that have the specified height, in
         pixels. You may use this filter with the size filter to return small
         images that have a height of 150 pixels.
        :type height: int
        :param id: An ID that uniquely identifies an image. Use this parameter
         to ensure that the specified image is the first image in the list of
         images that Bing returns. The
         [Image](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         object's imageId field contains the ID that you set this parameter to.
        :type id: str
        :param image_content: Filter images by the following content types.
         Face: Return images that show only a person's face. Portrait: Return
         images that show only a person's head and shoulders. Possible values
         include: 'Face', 'Portrait'
        :type image_content: str or
         ~azure.bing.search.customimagesearch.models.ImageContent
        :param image_type: Filter images by the following image types.
         AnimatedGif: Return only animated GIFs. Clipart: Return only clip art
         images. Line: Return only line drawings. Photo: Return only
         photographs(excluding line drawings, animated Gifs, and clip art).
         Shopping: Return only images that contain items where Bing knows of a
         merchant that is selling the items. This option is valid in the en -
         US market only.Transparent: Return only images with a transparent
         background. Possible values include: 'AnimatedGif', 'Clipart', 'Line',
         'Photo', 'Shopping', 'Transparent'
        :type image_type: str or
         ~azure.bing.search.customimagesearch.models.ImageType
        :param license: Filter images by the following license types. All: Do
         not filter by license type.Specifying this value is the same as not
         specifying the license parameter. Any: Return images that are under
         any license type. The response doesn't include images that do not
         specify a license or the license is unknown. Public: Return images
         where the creator has waived their exclusive rights, to the fullest
         extent allowed by law. Share: Return images that may be shared with
         others. Changing or editing the image might not be allowed. Also,
         modifying, sharing, and using the image for commercial purposes might
         not be allowed. Typically, this option returns the most images.
         ShareCommercially: Return images that may be shared with others for
         personal or commercial purposes. Changing or editing the image might
         not be allowed. Modify: Return images that may be modified, shared,
         and used. Changing or editing the image might not be allowed.
         Modifying, sharing, and using the image for commercial purposes might
         not be allowed. ModifyCommercially: Return images that may be
         modified, shared, and used for personal or commercial purposes.
         Typically, this option returns the fewest images. For more information
         about these license types, see [Filter Images By License
         Type](http://go.microsoft.com/fwlink/?LinkId=309768). Possible values
         include: 'All', 'Any', 'Public', 'Share', 'ShareCommercially',
         'Modify', 'ModifyCommercially'
        :type license: str or
         ~azure.bing.search.customimagesearch.models.ImageLicense
        :param market: The market where the results come from. Typically, mkt
         is the country where the user is making the request from. However, it
         could be a different country if the user is not located in a country
         where Bing delivers results. The market must be in the form <language
         code>-<country code>. For example, en-US. The string is case
         insensitive. For a list of possible market values, see [Market
         Codes](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview).
         NOTE: If known, you are encouraged to always specify the market.
         Specifying the market helps Bing route the request and return an
         appropriate and optimal response. If you specify a market that is not
         listed in [Market
         Codes](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview),
         Bing uses a best fit market code based on an internal mapping that is
         subject to change. This parameter and the
         [cc](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         query parameter are mutually exclusive—do not specify both.
        :type market: str
        :param max_file_size: Filter images that are less than or equal to the
         specified file size. The maximum file size that you may specify is
         520,192 bytes. If you specify a larger value, the API uses 520,192. It
         is possible that the response may include images that are slightly
         larger than the specified maximum. You may specify this filter and
         minFileSize to filter images within a range of file sizes.
        :type max_file_size: long
        :param max_height: Filter images that have a height that is less than
         or equal to the specified height. Specify the height in pixels. You
         may specify this filter and minHeight to filter images within a range
         of heights. This filter and the height filter are mutually exclusive.
        :type max_height: long
        :param max_width: Filter images that have a width that is less than or
         equal to the specified width. Specify the width in pixels. You may
         specify this filter and maxWidth to filter images within a range of
         widths. This filter and the width filter are mutually exclusive.
        :type max_width: long
        :param min_file_size: Filter images that are greater than or equal to
         the specified file size. The maximum file size that you may specify is
         520,192 bytes. If you specify a larger value, the API uses 520,192. It
         is possible that the response may include images that are slightly
         smaller than the specified minimum. You may specify this filter and
         maxFileSize to filter images within a range of file sizes.
        :type min_file_size: long
        :param min_height: Filter images that have a height that is greater
         than or equal to the specified height. Specify the height in pixels.
         You may specify this filter and maxHeight to filter images within a
         range of heights. This filter and the height filter are mutually
         exclusive.
        :type min_height: long
        :param min_width: Filter images that have a width that is greater than
         or equal to the specified width. Specify the width in pixels. You may
         specify this filter and maxWidth to filter images within a range of
         widths. This filter and the width filter are mutually exclusive.
        :type min_width: long
        :param offset: The zero-based offset that indicates the number of
         images to skip before returning images. The default is 0. The offset
         should be less than
         ([totalEstimatedMatches](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         - count). Use this parameter along with the count parameter to page
         results. For example, if your user interface displays 20 images per
         page, set count to 20 and offset to 0 to get the first page of
         results. For each subsequent page, increment offset by 20 (for
         example, 0, 20, 40). It is possible for multiple pages to include some
         overlap in results. To prevent duplicates, see
         [nextOffset](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview).
         Use this parameter only with the Image API. Do not specify this
         parameter when calling the Trending Images API or the Web Search API.
        :type offset: long
        :param safe_search: Filter images for adult content. The following are
         the possible filter values. Off: May return images with adult content.
         If the request is through the Image Search API, the response includes
         thumbnail images that are clear (non-fuzzy). However, if the request
         is through the Web Search API, the response includes thumbnail images
         that are pixelated (fuzzy). Moderate: If the request is through the
         Image Search API, the response doesn't include images with adult
         content. If the request is through the Web Search API, the response
         may include images with adult content (the thumbnail images are
         pixelated (fuzzy)). Strict: Do not return images with adult content.
         The default is Moderate. If the request comes from a market that
         Bing's adult policy requires that safeSearch is set to Strict, Bing
         ignores the safeSearch value and uses Strict. If you use the site:
         query operator, there is the chance that the response may contain
         adult content regardless of what the safeSearch query parameter is set
         to. Use site: only if you are aware of the content on the site and
         your scenario supports the possibility of adult content. Possible
         values include: 'Off', 'Moderate', 'Strict'
        :type safe_search: str or
         ~azure.bing.search.customimagesearch.models.SafeSearch
        :param size: Filter images by the following sizes. All: Do not filter
         by size. Specifying this value is the same as not specifying the size
         parameter. Small: Return images that are less than 200x200 pixels.
         Medium: Return images that are greater than or equal to 200x200 pixels
         but less than 500x500 pixels. Large: Return images that are 500x500
         pixels or larger. Wallpaper: Return wallpaper images. You may use this
         parameter along with the height or width parameters. For example, you
         may use height and size to request small images that are 150 pixels
         tall. Possible values include: 'All', 'Small', 'Medium', 'Large',
         'Wallpaper'
        :type size: str or
         ~azure.bing.search.customimagesearch.models.ImageSize
        :param set_lang: The language to use for user interface strings.
         Specify the language using the ISO 639-1 2-letter language code. For
         example, the language code for English is EN. The default is EN
         (English). Although optional, you should always specify the language.
         Typically, you set setLang to the same language specified by mkt
         unless the user wants the user interface strings displayed in a
         different language. This parameter and the
         [Accept-Language](https://docs.microsoft.com/en-us/bing/bing-custom-search/overview)
         header are mutually exclusive; do not specify both. A user interface
         string is a string that's used as a label in a user interface. There
         are few user interface strings in the JSON response objects. Also, any
         links to Bing.com properties in the response objects apply the
         specified language.
        :type set_lang: str
        :param width: Filter images that have the specified width, in pixels.
         You may use this filter with the size filter to return small images
         that have a width of 150 pixels.
        :type width: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Images or ClientRawResponse if raw=true
        :rtype: ~azure.bing.search.customimagesearch.models.Images or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.bing.search.customimagesearch.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.image_search.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['customConfig'] = self._serialize.query("custom_config", custom_config, 'str')
        if aspect is not None:
            query_parameters['aspect'] = self._serialize.query("aspect", aspect, 'str')
        if color is not None:
            query_parameters['color'] = self._serialize.query("color", color, 'str')
        if country_code is not None:
            query_parameters['cc'] = self._serialize.query("country_code", country_code, 'str')
        if count is not None:
            query_parameters['count'] = self._serialize.query("count", count, 'int')
        if freshness is not None:
            query_parameters['freshness'] = self._serialize.query("freshness", freshness, 'str')
        if height is not None:
            query_parameters['height'] = self._serialize.query("height", height, 'int')
        if id is not None:
            query_parameters['id'] = self._serialize.query("id", id, 'str')
        if image_content is not None:
            query_parameters['imageContent'] = self._serialize.query("image_content", image_content, 'str')
        if image_type is not None:
            query_parameters['imageType'] = self._serialize.query("image_type", image_type, 'str')
        if license is not None:
            query_parameters['license'] = self._serialize.query("license", license, 'str')
        if market is not None:
            query_parameters['mkt'] = self._serialize.query("market", market, 'str')
        if max_file_size is not None:
            query_parameters['maxFileSize'] = self._serialize.query("max_file_size", max_file_size, 'long')
        if max_height is not None:
            query_parameters['maxHeight'] = self._serialize.query("max_height", max_height, 'long')
        if max_width is not None:
            query_parameters['maxWidth'] = self._serialize.query("max_width", max_width, 'long')
        if min_file_size is not None:
            query_parameters['minFileSize'] = self._serialize.query("min_file_size", min_file_size, 'long')
        if min_height is not None:
            query_parameters['minHeight'] = self._serialize.query("min_height", min_height, 'long')
        if min_width is not None:
            query_parameters['minWidth'] = self._serialize.query("min_width", min_width, 'long')
        if offset is not None:
            query_parameters['offset'] = self._serialize.query("offset", offset, 'long')
        query_parameters['q'] = self._serialize.query("query", query, 'str')
        if safe_search is not None:
            query_parameters['safeSearch'] = self._serialize.query("safe_search", safe_search, 'str')
        if size is not None:
            query_parameters['size'] = self._serialize.query("size", size, 'str')
        if set_lang is not None:
            query_parameters['setLang'] = self._serialize.query("set_lang", set_lang, 'str')
        if width is not None:
            query_parameters['width'] = self._serialize.query("width", width, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['X-BingApis-SDK'] = self._serialize.header("self.x_bing_apis_sdk", self.x_bing_apis_sdk, 'str')
        if accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("accept_language", accept_language, 'str')
        if user_agent is not None:
            header_parameters['User-Agent'] = self._serialize.header("user_agent", user_agent, 'str')
        if client_id is not None:
            header_parameters['X-MSEdge-ClientID'] = self._serialize.header("client_id", client_id, 'str')
        if client_ip is not None:
            header_parameters['X-MSEdge-ClientIP'] = self._serialize.header("client_ip", client_ip, 'str')
        if location is not None:
            header_parameters['X-Search-Location'] = self._serialize.header("location", location, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Images', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    image_search.metadata = {'url': '/images/search'}
