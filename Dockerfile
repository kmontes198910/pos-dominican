# Use Odoo as a base image
FROM odoo:18.0

# Set build arguments
ARG BUILD_DATE

# Metadata
LABEL Name="medinec" \
      Version="0.0.1" \
      Email="example@company.com" \
      Vendor="KyNSoft" \
      build_date="${BUILD_DATE}"

# Copy and install Python dependencies
COPY ./requirements.txt /app/requirements.txt

# because of changes in Odoo's odoo:18.0 image to modify the default behavior of pip
# to not use the --break-system-packages flag, we need to explicitly set it here
RUN pip install --no-cache-dir --break-system-packages -r /app/requirements.txt

# Copy custom configuration
COPY ./conf/odoo.conf /etc/odoo/odoo.conf

# Copy custom add-ons with proper ownership
COPY --chown=odoo:odoo ./extra-addons /mnt/extra-addons
