import React from 'react';
import PropTypes from 'prop-types';
import ReactMarkdown from 'react-markdown';
import shortcodes from 'remark-shortcodes';
import Map from './Map';

const components = {
    Map: Map,
};

const getComponent = identifier => components[identifier];

const sanitizeAttribute = data => {
    if (typeof data === 'string') {
        const lastCharIndex = data.length - 1;
        const firstChar = data[0];
        const lastChar = data[lastCharIndex];
        if (firstChar === "'" && lastChar === "'") {
            return data.substring(1, lastCharIndex);
        }
        return data;
    }
};

const ShortcodeRenderer = ({identifier, attributes}) => {
    const keys = Object.keys(attributes);
    const sanitizedAttributes = {};
    keys.forEach(key => {
        sanitizedAttributes[key] = sanitizeAttribute(attributes[key]);
    });
    const Component = getComponent(identifier);
    return <Component {...sanitizedAttributes} />;
};

const Markdown = ({children, ...props}) => (
    <ReactMarkdown
        source={Array.isArray(children) ? children.join('\n') : children}
        escapeHtml={true}
        plugins={[[shortcodes]]}
        renderers={{
            shortcode: ShortcodeRenderer,
        }}
        {...props}
    />
);

Markdown.propTypes = {
    id: PropTypes.string,
    /**
     * Class name of the container element
     */
    className: PropTypes.string,

    /**
     * An object containing custom element props to put on the container
     * element such as id or style
     */
    containerProps: PropTypes.object,

    /**
     * A markdown string (or array of strings) that adhreres to the CommonMark spec
     */
    children: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string),
    ]),

    /**
     * A object for execution instructions
     */
    renderers: PropTypes.object,
    /**
     *
     */
    components: PropTypes.object,
};

export default Markdown;
