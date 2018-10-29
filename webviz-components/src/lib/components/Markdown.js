import React from 'react';
import PropTypes from 'prop-types';
import ReactMarkdown from 'react-markdown';
import shortcodes from 'remark-shortcodes';

// eslint-disable-next-line valid-jsdoc
/**
 * A component that renders Markdown text as specified by the
 * CommonMark spec.
 */
const Markdown = ({children, renderers, components, ...props}) => (
    <ReactMarkdown
        source={Array.isArray(children) ? children.join('\n') : children}
        escapeHtml={true}
        plugins={[shortcodes]}
        // renderers={{
        //     shortcodes: ({identifier, attributes}) => {
        //         console.log('identifier', identifier);
        //         console.log('attributes', attributes);
        //         console.log('components', components);
        //         return components[identifier](attributes);
        //     },
        // }}
        renderers={{}}
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
